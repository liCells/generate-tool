import argparse
import openai
import platform
import json

def main():
    parser = argparse.ArgumentParser(description="Generate script based on user's requirements.")
    parser.add_argument("-k", "--api_key", help="API key for OpenAI.", required=True)
    parser.add_argument("-v", "--api_version", choices=["3.5-turbo", "4", "4-turbo-preview"], default="4-turbo-preview", help="API version to use: GPT-3.5 Turbo, GPT-4, or GPT-4 Turbo Preview. Default is GPT-4 Turbo Preview.")
    parser.add_argument("-content", "--key_content", help="The content to be included in the prompt.", required=True)
    parser.add_argument("-t", "--script_type", help="The type of script to generate.", required=True)
    parser.add_argument("-f", "--script_file", help="The script file name to generate.", required=True)
    args = parser.parse_args()

    openai.api_key = args.api_key
    user_env = platform.system() + " " + platform.machine()  # Example: Windows AMD64

    engine_map = {
        "3.5-turbo": "gpt-3.5-turbo",
        "4": "gpt-4",
        "4-turbo-preview": "gpt-4-turbo-preview"
    }
    engine = engine_map[args.api_version]
    prompt = f"""
    你是一位专业的技术人员，且擅长编写{args.script_type}脚本，我希望你能通过一个{args.script_type}脚本帮我实现以下功能。
    规则：
    1. 只返回脚本代码
    2. 如果有不明确的参数，设置为用户输入的形式，例：script -name test
    3. 如果有不明确的地方，不返回代码，返回问题
    4. 对于密码需要交互式输入而非明文输入
    5. 严格按照脚本代码的json格式进行返回
    要求：{args.key_content}
    用户环境：{user_env}
    脚本代码例子：
    {{
      "script": "python export.py",
      "usage": "详细信息可通过 python export.py -h 查看",
      "depend": "此脚本假设您已经有Python环境以及必要的库（pymysql和csv）。如果没有，请先安装这些库。您可以通过运行 `pip install pymysql` 安装pymysql库",
      "question": ""
    }}
    脚本代码：
    {{
      "script": "",
      "usage": "",
      "depend": "",
      "question": ""
    }}
    """

    try:
        response = openai.chat.completions.create(
            model=engine,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        json_data = response.choices[0].message.content.strip()[7:-3]
        # 解析JSON
        parsed_data = json.loads(json_data)

        # 获取script内容并写入到文件中
        with open(args.script_file, 'w') as script_file:
            script_file.write(parsed_data['script'])

        # 打印usage和depend
        print("Usage:")
        print(parsed_data['usage'])
        print("\nDependency:")
        print(parsed_data['depend'])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

