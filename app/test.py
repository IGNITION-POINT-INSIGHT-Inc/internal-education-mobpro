# import openai
from openai import OpenAI
import os

def get_openai_response(prompt):
    # 環境変数からAPIキーを取得
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "日本の首都は？",
                }
            ],
            model="gpt-4o",
        )
        # # OpenAIのChatCompletionエンドポイントを呼び出す
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",  # 使用するモデルを指定
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": prompt}
        #     ]
        # )

        # レスポンスからテキストを抽出
        # message = response.choices[0].message['content']
        print(response.choices[0].message.content)
        # return message
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

# 使用例
prompt = "Hello, how are you?"
response = get_openai_response(prompt)
print(response)