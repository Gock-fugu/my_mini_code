import speedtest

st = speedtest.speedtest()
st.get_best_server()

ping = st.results.ping
download = st.download()
upload = st.upload()

print(ping, download*100, upload*100)