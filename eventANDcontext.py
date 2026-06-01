def lambda_handler(event, context):

    print("Name: ", event['name'])

    print("Function Name:", context.function_name)

    print("Function Version:", context.function_version)

    print("Request ID:", context.aws_request_id)

    print("Memory:", context.memory_limit_in_mb)

    print("Log Group:", context.log_group_name)

    print("Log Stream:", context.log_stream_name)

    print("ARN:", context.invoked_function_arn)

    print("Remaining Time:",
          context.get_remaining_time_in_millis())

    return {
        "statusCode": 200
    }
