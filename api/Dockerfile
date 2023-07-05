FROM python:3.11

# Create the workdir
WORKDIR /app

# Copy the code to the workdir
COPY . /app

# Install the app requirements
RUN pip install -r requirements.txt

# Expose the app port
EXPOSE 8000

# Run the setup script and start the Flask app with a sleep command
CMD python chelsea_players.py && uvicorn main:app --host=0.0.0.0 --port=8000