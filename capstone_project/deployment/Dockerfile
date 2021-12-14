FROM public.ecr.aws/lambda/python:3.8

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl
RUN pip install Pillow
RUN pip install requests

COPY best_model.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]

