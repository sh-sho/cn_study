FROM fnproject/python:3.9-dev as build-stage

ENV TMPDIR=/mnt/blockvol1/tmp
WORKDIR /function
ADD requirements.txt /function/

                        RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
                            rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
                            chmod -R o+r /python &&\
                            groupadd --gid 1000 fn && \
                            adduser --uid 1000 --gid fn fn
ADD . /function/
RUN rm -fr /function/.pip_cache
FROM fnproject/python:3.9
WORKDIR /function
COPY --from=build-stage /python /python
COPY --from=build-stage /function /function
RUN chmod -R o+r /function
ENV PYTHONPATH=/function:/python
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]