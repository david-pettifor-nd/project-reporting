FROM python:2.7
ENV PYTHONUNBUFFERED 1

# Make a location for all of our stuff to go into
RUN mkdir /code

# Set the working directory to this new location
WORKDIR /code

# Copy all of our scripts into the location
ADD requirements.txt /code/

# Install requirements for Django
RUN pip install -r requirements.txt

# Add our Django code
ADD . /code/

# Expose the port so we can access Django as it's running
EXPOSE 8000

# Set the entry point script
#ADD docker_django/wait_for_postgres.sh /code/
#ADD docker_django/wait_for_postgres.py /code/
#RUN chmod +x /code/docker_django/wait_for_postgres.sh

ENTRYPOINT ["/code/docker_django/wait_for_postgres.sh"]

# Start the server:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]