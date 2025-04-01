from helpers.glue_service import start_glue_job

def lambda_handler(event, context):
    print(event)

    try:
        start_glue_job("glue-job-name")
        return{
            'statusCode': 200,
            'body': "Job do Glue iniciado com sucesso"
        }
    except:
        return {
            'statusCode': 500,
            'body': "Erro ao iniciar o job do Glue"
        }
