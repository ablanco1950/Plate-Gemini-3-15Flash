# Plate-Gemini-3-15Flash
Recognizing license plates by calling Gemini-3-15Flash from a Python program.

Installation:

Install the official Google Gen AI SDK:

pip install google-genai pillow

A requirements.txt file is included.

Obtain the Google API key at:

https://aistudio.google.com/api-keys?project=gen-lang-client-0252907537

Click the "Create API key" button, and then on the next screen, click the "Create key" button again. Ignore the fields for project name and other fields; a default project name will appear.

Copy the API key obtained on line 16 of the Test.py program.

Unpack the file containing the test images, Test1.zip.

Run the test program:

Test.py

The program displays the license plate text one by one. To continue, press Enter.

By changing line 62 of the program, you can test any image folder.

Conclusions:

Despite the limited free trial period offered by Google, the following can be noted:

- The OCR and license plate detection work with great accuracy. The image CY110KS.jpg is difficult for other OCR programs to recognize.

- Despite the prompt instructions, the license plates in images 8544.jpg and 2122267.jpg appear formatted with hyphens. Perhaps because Google AI has classified them as corresponding to countries with that format.

- The Gemini-3-15Flash server is often overwhelmed, displaying the message "Error connecting to the Gemini API: 503 UNAVAILABLE." {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

Can test the capabilities of Gemini-3-5-flash  as OCR through this Roboflow page:

https://playground.roboflow.com/models/google/gemini-3-5-flash?utm_campaign=Newsletter+-+5%2F21%2F2026+-+%5Bcvpr%5D&utm_content=Newsletter+-5%2F21%2F2026+-+cvpr&utm_medium=email_action&utm_source=email
