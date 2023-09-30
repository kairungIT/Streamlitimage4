import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
st.title("Streamlit WebRTC Example")

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class VideoProcessor:
	def recv(self,frame):
			frm=frame.to_narray(format='bgr24')
			faces=cascade.detectMultiScale(cv2.cvtColor(frm,cv2.COLOR_BGR2GRAY),1.1,3)
			for x,y,w,h in faces:
				cv2.rectangle(frm,(x,y),(x+w,y+h),(0,255,0),3)
			return av.VideoFrame.from_ndarray(frm, format='bgr24')
				
#if st.button('show video'):
webrtc_streamer(key="key",video_processor_factory=VideoProcessor)