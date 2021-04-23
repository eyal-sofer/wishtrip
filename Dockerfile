FROM python:3
2	# Set application working directory
3	WORKDIR /usr/src/app
4	# Install requirements
5	COPY requirements.txt ./
6	RUN pip install --no-cache-dir -r requirements.txt
7	# Install application
8	COPY app.py ./
9	# Run application
10	CMD python app.py
