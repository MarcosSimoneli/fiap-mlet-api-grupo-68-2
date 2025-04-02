import boto3

def start_glue_job(job_name):
    # Instanciando o cliente do Glue
    glue_client = boto3.client('glue')
    
    # Nome do job do Glue
    job_name = 'nome-do-seu-job-glue'
    
    try:
        # Acionando o job do Glue
        response = glue_client.start_job_run(JobName=job_name)
        print(f"Job {job_name} iniciado com sucesso. JobRunId: {response['JobRunId']}")
        return {
            'statusCode': 200,
            'body': f"Job {job_name} iniciado com sucesso. JobRunId: {response['JobRunId']}"
        }
    except Exception as e:
        print(f"Erro ao iniciar o job do Glue: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Erro ao iniciar o job do Glue: {str(e)}"
        }