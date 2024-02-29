# gearbox
Comend's project repo for the AI model controller/API.
This API is interfaced by several of Comend's core products including [Librarey](https://github.com/comendcare/mesa) and [Scimantic](https://github.com/comendcare/livery) frontends.

## Structure
This is a simple REST API served by Flask. We use a mix of services, composed by factories that are controlled by facades to serve responses.

## Installation
You can install the dependencies of this project with `pip install -r requirements.txt`.

## Usage
This project is meant to be used exclusively through the frontends of Comend products, not as a general purpose API.

If this is your first time running this locally, you'll need to create a `logs` directory in the root directory.
To get the the Flask API server started locally, you'll need a `.env` file with the correct environment variables.
Once you have the environment variables set up, you can start the server by running `main.py`.

## Deployment
### Cloud console and command line
Deployment of this API is done with Google Cloud Run via the Google Cloud Console.

Alternatively you can also create a new deployment in the command line using `gcloud init` (if it's the first time deploying this proejct) and running `gcloud run deploy`.
Be sure to set the current working project using `gcloud config set project PROJECT_ID`.
You may be asked to select a region for the server and other configuration details.
It may help to follow the steps outlined in this guide [here](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

### Setting environment variables
This project requires certain environment variables to be set up. For example the `ENVIRONMENT` variable, and the `OPENAI_API_KEY` variable.
You can set these variables in Google Cloud Console and deploy a revision of the cloud run instance to publish the changes.

## Stack
| Package  | Use Case                                               |
|----------|--------------------------------------------------------|
| Flask    | To build and serve our API endpoints.                  |
| Pydantic | To validate json in requests and responses to the API. |
| OpenAI   | Our main AI API from which we use to generate output.  |
