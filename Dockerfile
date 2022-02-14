FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Make a location for all of our stuff to go into
RUN mkdir /app

# Set the working directory to this new location
WORKDIR /app

# Copy all of our scripts into the location
ADD requirements.txt /app/

# Install requirements for Django
RUN pip install -r requirements.txt

# Add our Django code
ADD . /app/

# Expose the port so we can access Django as it's running
EXPOSE 8000

# Set the entry point script
ADD wait_for_postgres.sh /app/
ADD wait_for_postgres.py /app/
RUN chmod +x /app/wait_for_postgres.sh

ENTRYPOINT ["/app/wait_for_postgres.sh"]

# Start the server:
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]