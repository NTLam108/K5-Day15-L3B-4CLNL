"""Kiểm tra hợp đồng kết nối OpenAI và Groq, không gửi request thật."""
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codebase"))
import ai


class Response(io.BytesIO):
    def __init__(self):
        super().__init__(json.dumps({"model": "model-test", "choices": [{"message": {"content": "trả lời"}}],
                                     "usage": {"prompt_tokens": 12, "completion_tokens": 7}}).encode())


class ModelConnectionTests(unittest.TestCase):
    def test_providers_use_correct_endpoint_and_api_usage(self):
        for provider, host in (("openai", "api.openai.com"), ("groq", "api.groq.com")):
            with self.subTest(provider=provider), patch.object(ai, "MODEL_PROVIDER", provider), \
                    patch.object(ai, "MODEL_NAME", "model-test"), patch.object(ai, "API_KEY", "test-key"), \
                    patch("ai.urllib.request.urlopen", return_value=Response()) as request:
                result = ai.call_model("system", "user")
                self.assertIn(host, request.call_args.args[0].full_url)
                self.assertEqual(result, {"text": "trả lời", "model": "model-test", "tokens_in": 12, "tokens_out": 7})


if __name__ == "__main__":
    unittest.main()
