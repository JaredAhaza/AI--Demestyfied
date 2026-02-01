"""
Voice Engine - Text-to-Speech using ElevenLabs
"""

import os
import requests
import sys

class VoiceEngine:
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = os.getenv("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
        
        # Windows encoding safety
        self.safe_stdout = sys.stdout

    def _safe_print(self, text):
        try:
            print(text)
        except UnicodeEncodeError:
            if hasattr(self.safe_stdout, 'buffer'):
                self.safe_stdout.buffer.write(text.encode('utf-8'))
                self.safe_stdout.buffer.write(b'\n')

    def generate_audio(self, text: str):
        """
        Generate audio from text using ElevenLabs API.
        Returns:
            bytes: Audio content
        """
        if not self.api_key or "your_elevenlabs_key" in self.api_key:
            self._safe_print("⚠️ ElevenLabs API key not configured.")
            return None

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            
            if response.status_code == 200:
                self._safe_print("✅ Audio generated successfully!")
                return response.content
            else:
                self._safe_print(f"⚠️ ElevenLabs Error: {response.text}")
                return None
                
        except Exception as e:
            self._safe_print(f"⚠️ Error formatting voice request: {e}")
            return None
