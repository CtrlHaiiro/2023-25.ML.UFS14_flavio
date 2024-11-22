
# PER COSTRUIRE I DATI IN INGRESSO USATI DA INFERENZA
JSON_IN_INGRESSO_PER_INFERENZA='{"Square_Footage": 12.2, "....": 1234}'
JSON_IN_INGRESSO_PER_INFERENZA_B64=printf $JSON_IN_INGRESSO_PER_INFERENZA | base64

# PER SVOLGERE L'INFERENZA
/usr/local/bin/aws sagemaker-runtime invoke-endpoint --endpoint-name 'la-mia-prima-api-inferenza' --body "${JSON_IN_INGRESSO_PER_INFERENZA_B64}" inference-response.json

# PER VEDERE LA RISPOSTA DELL'INFERENZA
cat inference-response.json