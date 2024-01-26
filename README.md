# EcoVision

## Overview
This project utilizes YOLOv8 for object detection, with a focus on fine-tuning the model to suit specific requirements. The implementation includes a Python Flask API hosted on Azure, allowing users to upload images for real-time processing and view the results.

## Features
- YOLOv8 object detection
- Fine-tuned model for specific use cases
- Azure cloud services for image upload and processing
- Python Flask API for seamless integration
- Live demo link: [Live Demo](https://rohitsk2003.pythonanywhere.com/)
- Video Summary: [YouTube Video](https://youtu.be/g9UyXD49NL4)

## Getting Started

### Prerequisites
- Python 
- YOLOv8
- Azure Storage Account 
- Flask

### Usage
1. Run the Flask app: `python app.py`
2. Open a web browser and navigate to [http://localhost:3000/](http://localhost:3000/)
3. Upload an image and explore the real-time processing capabilities.
4. For finding the geolocation make sure the image has latitude and longitude information as metadata ( check image properties->details->GPS).
5. We have made finding geolocation alone offline , download two files GeoTagExtractor.py, main-geo.py and finally make sure both are in same directory.
6. Use main-geo.py and copy paste the image local path to it and run the python file.
7. You would receive a link, by clicking on it you would be directed the Google Maps.

## Contribution Guidelines
- Fork the repository
- Create a new branch: `git checkout -b feature/new-feature`
- Commit your changes: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature/new-feature`
- Create a pull request

## Acknowledgments
- Mention any contributors or libraries you've used.
- Provide credits or references to the original YOLOv8 repository.

