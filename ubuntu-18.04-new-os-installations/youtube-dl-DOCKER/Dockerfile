# Use official Python image
FROM python:3.9-slim

# Install ffmpeg (required for some conversions)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Install yt-dlp
RUN pip install yt-dlp

# Copy your script into the container
COPY downloader.py /app/downloader.py

# Set working directory
WORKDIR /app

# Set entrypoint (default command)
ENTRYPOINT ["python", "downloader.py"]