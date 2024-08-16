# gearbox
Comend's project repo for the AI model controller/API.
This API is interfaced by several of Comend's core products including [Librarey](https://github.com/comendcare/mesa) and [Scimantic](https://github.com/comendcare/livery) frontends.

## Structure
This is a simple REST API served by Flask. We use a mix of services, composed by factories that are controlled by facades to serve responses.

## Development Environment Setup

### Prerequisites
1. Python 3.11 - download the v3.11 installer [here](https://www.python.org/downloads/release/python-3110/)
> Note: To double check your installed python version you can run one of the following commands in the terminal `python --version` OR `python3 --version`

### Installation Steps
1. Clone the gearbox repo
2. Setup Env Variables - Create a `.env` file in the gearbox root directory (ask a team member for the environment variable contents)
3. Install dependencies - Run `pip install -r requirements.txt` in the root directory
> Note: if you have issues using `pip` you can also use `pip3`

> Note: if you encounter the following error message `ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (aiohttp)` double check that you have the proper python version installed.
4. Setup Logs - Create a `logs` directory in the gearbox root directory
5. Run the `main.py` file to start the server! - run `python main.py`

### Checking proper installation
To double check that you have installed, and are running the server properly:
1. Start the server - `python main.py`
2. Send the following POST request with your preferred method (see below). The server should respond with a summary of the user text.

> Note: if you run into the following error while checking your installation `openai.error.APIConnectionError: Error communicating with OpenAI` you may need to manually install the required python certificates. To do so, run `bash /Applications/Python*/Install\ Certificates.command`
>
> https://stackoverflow.com/questions/75920597/openai-error-apiconnectionerror-error-communicating-with-openai

**Method 1: Curl command**
``` bash
curl --location 'http://127.0.0.1:5000/translate' \
--header 'Content-Type: application/json' \
--data '{
    "task": "TRANSLATION",
    "data": {
        "user_text": "Warsaw breakage syndrome (WABS) is a very rare recessive hereditary disease caused by mutations in the gene coding for the DNA helicase DDX11, involved in genome stability maintenance and sister cohesion establishment. Typical clinical features observed in WABS patients include growth retardation, facial dysmorphia, microcephaly, hearing loss due to cochlear malformations and, at cytological level, sister chromatid cohesion defects. Molecular bases of WABS have not yet been elucidated, due to lack of disease animal model systems and limited knowledge of the DDX11 physiological functions. However, WABS is considered to belong to the group of cohesinopathies, genetic disorders due to mutations of subunits or regulators of cohesin, the protein complex responsible for tethering sister chromatids from the time of their synthesis till they separate in mitosis. Recent evidences suggest that cohesin and its regulators have additional key roles in chromatin organization by promoting the formation of chromatin loops.function of cohesin is expected to impact gene transcription during cell differentiation and embryonic development and its dis-regulation, caused by mutation/loss of genes encoding cohesin subunits or regulators, could originate the developmental defects observed in cohesinopathies. Ethiopathogenesis of WABS is discussed in line with these recent findings and evidence of a possible role of DDX11 as a cohesin regulator.",
        "audience": "FAMILY",
        "readability": 0.2,
        "tone": "EMPATHETIC",
        "temperature": 0.2,
        "max_tokens": 3000
    }
}'
```

**Method 2: GUI**

Send the following request in an app like [insomnia](https://insomnia.rest/download) or [postman](https://www.postman.com/downloads/)

- POST location: http://127.0.0.1:5000/translate
- Header: "Content-Type": "application/json"
- Body:
```
{
    "task": "TRANSLATION",
    "data": {
        "user_text": "Warsaw breakage syndrome (WABS) is a very rare recessive hereditary disease caused by mutations in the gene coding for the DNA helicase DDX11, involved in genome stability maintenance and sister cohesion establishment. Typical clinical features observed in WABS patients include growth retardation, facial dysmorphia, microcephaly, hearing loss due to cochlear malformations and, at cytological level, sister chromatid cohesion defects. Molecular bases of WABS have not yet been elucidated, due to lack of disease animal model systems and limited knowledge of the DDX11 physiological functions. However, WABS is considered to belong to the group of cohesinopathies, genetic disorders due to mutations of subunits or regulators of cohesin, the protein complex responsible for tethering sister chromatids from the time of their synthesis till they separate in mitosis. Recent evidences suggest that cohesin and its regulators have additional key roles in chromatin organization by promoting the formation of chromatin loops.function of cohesin is expected to impact gene transcription during cell differentiation and embryonic development and its dis-regulation, caused by mutation/loss of genes encoding cohesin subunits or regulators, could originate the developmental defects observed in cohesinopathies. Ethiopathogenesis of WABS is discussed in line with these recent findings and evidence of a possible role of DDX11 as a cohesin regulator.",
        "audience": "FAMILY",
        "readability": 0.2,
        "tone": "EMPATHETIC",
        "temperature": 0.2,
        "max_tokens": 3000
    }
}
```

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
