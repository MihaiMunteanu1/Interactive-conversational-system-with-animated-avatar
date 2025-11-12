from transformers import AutoModelForCausalLM, AutoTokenizer
from proiect.ChatAssistant.config import MODEL_NAME
from proiect.Utils.utils import handle_error


class QAAssistant:
    def __init__(self):
        self.model, self.tokenizer = self.load_model()
        self.chat_history = []

    @staticmethod
    def load_model():
        try:
            tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
            model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
            tokenizer.pad_token = tokenizer.eos_token
            return model, tokenizer
        except Exception as e:
            handle_error("Model loading failed", e)
            return None, None

    def ask(self, question):
        if not self.model or not self.tokenizer:
            return "[INFO] System not ready. Please restart."

        try:
            inputs = self.tokenizer.encode(
                question + self.tokenizer.eos_token,
                return_tensors='pt',
                max_length=512,
                truncation=True
            )

            outputs = self.model.generate(
                inputs,
                max_length=512,
                pad_token_id=self.tokenizer.eos_token_id,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                repetition_penalty=1.2
            )

            answer = self.tokenizer.decode(
                outputs[:, inputs.shape[-1]:][0],
                skip_special_tokens=True
            )
            return answer.strip()
        except Exception as e:
            handle_error("Response generation failed", e)
            return "I encountered an error. Could you repeat that?"