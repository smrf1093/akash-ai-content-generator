import openai
import textwrap
from django.conf import settings


class ArticleBuilder:
    """This class generates SEO-friendly articles for a blog in the context of Web3 and Blockchain"""

    def __init__(self, context="Web3 and Blockchain"):
        self.context = context
        self.bot_message_guidance = f"You are a content writer in the field of {self.context}. Write a well-structured and SEO-friendly article on the topic."
        self.system_message = [
            {
                "role": "system",
                "content": f"You are in a conversation with a content writer in the field of {self.context}. The writer will provide you with a well-structured and SEO-friendly article on the topic.",
            },
            {
                "role": "system",
                "content": "Please provide the topic and keywords for the article, and the writer will respond accordingly.",
            },
        ]

    def get_article(self, topic, keywords):
        client = openai.OpenAI(
            api_key=settings.OPENAI_API_KEY, base_url=settings.OPENAI_BASE_URL
        )

        messages = self.system_message + [
            {"role": "assistant", "content": self.bot_message_guidance},
            {
                "role": "user",
                "content": f"Write an article on the topic of '{topic}' incorporating the keywords '{keywords}'. The article should be well-structured, SEO-friendly, and at least 500 words.",
            },
        ]

        response = client.chat.completions.create(
            model=settings.DEFAULT_MODEL, messages=messages, max_tokens=2048
        )

        article = response.choices[0].message.content
        return article

    def optimize_article(self, article, keywords):
        # Optimize the article for SEO
        optimized_article = article
        for keyword in keywords.split(","):
            keyword = keyword.strip()
            optimized_article = optimized_article.replace(keyword, f"<b>{keyword}</b>")
        return optimized_article


# Example usage:
article_builder = ArticleBuilder(context="Web3 and Blockchain")
topic = "The Future of Blockchain Technology"
keywords = "blockchain, cryptocurrency, decentralized finance"
article = article_builder.get_article(topic, keywords)
optimized_article = article_builder.optimize_article(article, keywords)
print(optimized_article)
