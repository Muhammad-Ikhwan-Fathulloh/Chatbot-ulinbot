FROM rasa/rasa:3.1.0

COPY app /app
COPY server.sh /app/server.sh

USER root

RUN rasa train nlu
RUN chmod a+rwx /app/server.sh

ENTRYPOINT ["/app/server.sh"]