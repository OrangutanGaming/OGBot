FROM gorialis/discord.py:3.6.6-alpine-rewrite-minimal

WORKDIR /app

#RUN pip install -U git+https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice].git git+https://github.com/cburgmer/upsidedown.git

COPY requirements.txt ./
RUN pip install -U -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
