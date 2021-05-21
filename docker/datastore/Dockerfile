FROM google/cloud-sdk:341.0.0-alpine

ENV PATH="/scripts:$PATH"

RUN apk add --update --no-cache openjdk8-jre
RUN gcloud components install cloud-datastore-emulator --quiet

VOLUME /opt/data

COPY ./run.sh /scripts/run.sh
RUN chmod +x /scripts/*

CMD ["run.sh"]
