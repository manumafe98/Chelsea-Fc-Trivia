FROM python:3.11

# Create the workdir
WORKDIR /gui

# Copy the code to the workdir
COPY . /gui

# Install the app requirements
RUN pip install -r requirements.txt

# Run the ctkinter gui
CMD python main.py