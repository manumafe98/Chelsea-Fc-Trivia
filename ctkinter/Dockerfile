FROM python:3.11

# Create the workdir
WORKDIR /gui

# Copy the code to the workdir
COPY . /gui

# Give execution permissions to entrypoint.sh
RUN chmod +x /gui/entrypoint.sh

# Install the app requirements
RUN pip install -r requirements.txt
