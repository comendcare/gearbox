class IllustrationPromptBuilder:
    def __init__(self):
        self.prompt = """You are a highly skilled AI trained to generate images of any given prompt. 
                        I would like you to read the following prompt and generate an illustration for it."""

    def add_style(self, style):
        match style:
            case "VECTOR":
                self.prompt += """ Minimalist, clean, and sharp, vector artwork is comprised of straight lines and
                                    points with intentional curves."""
            case "REALISTIC":
                self.prompt += """ Detailed, natural, and most resembling what your prompt would look like in real life."""
            case "ARTISTIC":
                self.prompt += """ Creative, stylistic, and opinionated.
                                    Pair with more samples to generate several different styles."""
            case _:
                pass
        return self

    def build(self):
        return ' '.join(self.prompt.strip().split())

