from duckduckgo_search import DDGS


class Internet:

    @staticmethod
    def search(query):

        try:

            with DDGS() as ddgs:

                results = list(
                    ddgs.text(
                        query,
                        max_results=5
                    )
                )

            if not results:
                return None

            text = ""

            for i, result in enumerate(results, start=1):

                title = result.get("title", "")
                body = result.get("body", "")
                link = result.get("href", "")

                text += (
                    f"{i}. {title}\n"
                    f"{body}\n"
                    f"{link}\n\n"
                )

            return text

        except Exception as e:

            return str(e)