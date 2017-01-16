# EchoAutomation
Home automation using Amazon echo. To get this project running on your own echo, or using echosim.io follow these instructions
- Amazon Developer Console -
1. set up an amazon developer account https://developer.amazon.com
2. Create a new skill, you can use the sample intents.schema that we have under alexa files
3. add slots, add utterences
4. under configuration keep note of the end point, you will end up using an ngrok endpoint later so we will come back to this
5. under sll use  "My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority"

- Raspberry Pi - 
1. Wire any sensors and LEDs to your raspberry pi
2. if your sensors require i2c, i will have i2c instructions here in the next few days
3. start gpio_control.py, moving.py, and ./ngrok
4. copy the ngrok url into your configuration on your skill page, the ngrok url looks like this https://34b49265.ngrok.io

Then give your alexa any of your utterances and wait for a response.
