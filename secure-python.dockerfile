FROM amazonlinux:2023  

ENV PYTHON\_VERSION\=3.9  

RUN \--mount=type=cache,target=/var/cache/dnf \\  
    dnf \-y update && \\  
    dnf install \-y python${PYTHON\_VERSION} python${PYTHON\_VERSION}\-pip shadow\-utils git\-all findutils awscli tar && \\  
    update\-alternatives \--install /usr/bin/python python /usr/bin/python${PYTHON\_VERSION} 20 && \\  
    update\-alternatives \--set python /usr/bin/python${PYTHON\_VERSION} && \\  
    dnf clean all && \\ rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /usr/src/app  

COPY requirements.txt ./  

RUN pip install \--no-cache-dir -r requirements.txt  

COPY . .  