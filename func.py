import io
import json
import logging
import requests

from fdk import response

nvidia_url = "https://objectstorage.us-ashburn-1.oraclecloud.com/p/xik5PN53LN92vcDgAlQAjaWwajuJdEJSb7jxlNFCWCFcSnr2DFTrSv6xZgOTKIYP/n/hpc_limited_availability/b/Nvidia_Handover/o/"

def handler(ctx, data: io.BytesIO=None):
    # name = "World"
    # try:
    #     body = json.loads(data.getvalue())
    #     name = body.get("name")
    # except (Exception, ValueError) as ex:
    #     logging.getLogger().info('error parsing json payload: ' + str(ex))
    resp = None
    try:
        logging.getLogger().debug('payload: ' + str(data))
        resp = requests.put(data, nvidia_url)
    except Exception as ex:
        logging.getLogger().error('error parsing payload: ' + str(ex))

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Status {0}".format(resp.status_code)}),
        headers={"Content-Type": "application/json"}
    )
