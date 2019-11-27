from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

class VisionProcessor(object):

    def __init__(self):
        self.key = '3a87d7164ee54d478eef0fae83947846'
        self.endpoint = 'https://cv-dev-hackathon.cognitiveservices.azure.com/'

    def process(self):
        self.computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.key))
        '''
        Batch Read File, recognize printed text - remote
        This example will extract printed text in an image, then print results, line by line.
        This API call can also recognize handwriting (not shown).
        '''
        print("===== Batch Read File - remote =====")
        # Get an image with printed text
        remote_image_printed_text_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample" \
                                        "-data-files/master/ComputerVision/Images/printed_text.jpg"

        # Call API with URL and raw response (allows you to get the operation location)
        recognize_printed_results = self.computervision_client.batch_read_file(remote_image_printed_text_url, raw=True)

        # Get the operation location (URL with an ID at the end) from the response
        operation_location_remote = recognize_printed_results.headers["Operation-Location"]
        # Grab the ID from the URL
        operation_id = operation_location_remote.split("/")[-1]

        # Call the "GET" API and wait for it to retrieve the results
        while True:
            get_printed_text_results = self.computervision_client.get_read_operation_result(operation_id)
            if get_printed_text_results.status not in ['NotStarted', 'Running']:
                break
            time.sleep(1)

        # Print the detected text, line by line
        if get_printed_text_results.status == TextOperationStatusCodes.succeeded:
            for text_result in get_printed_text_results.recognition_results:
                for line in text_result.lines:
                    print(line.text)
                    print(line.bounding_box)


