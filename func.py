import io
import json
import logging
import requests

from fdk import response

nvidia_url = "https://objectstorage.us-ashburn-1.oraclecloud.com/p/xik5PN53LN92vcDgAlQAjaWwajuJdEJSb7jxlNFCWCFcSnr2DFTrSv6xZgOTKIYP/n/hpc_limited_availability/b/Nvidia_Handover/o/"

funcDefinition = {
    "status": {
        "returnCode": 0,
        "errorMessage": ""
    },
    "funcDescription": {
        "outputs": [],
        "parameters": [],
        "bucketName": "bucket-OCI-FAAS",
        "isOutputJoinableWithInput": True
    }
}


def handler(ctx, data: io.BytesIO=None):
    response_data = ""
    # DESCRIBE FUNCTION
    try:
        body = json.loads(data.getvalue())
        funcMode = body.get("funcMode")
        if funcMode == 'describeFunction':
           response_data = json.dumps(funcDefinition)
    except (Exception, ValueError) as ex:
        response_data = json.dumps(
            {"error": "{0}".format(str(ex))})
    # EXECUTE FUNCTION
    resp = None
    try:
        logging.getLogger().debug('payload: ' + str(data))
        resp = requests.put(data, nvidia_url)
    except Exception as ex:
        logging.getLogger().error('error parsing payload: ' + str(ex))

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Status {0}".format(resp)}),
        headers={"Content-Type": "application/json"}
    )
