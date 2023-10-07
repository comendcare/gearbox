class PromptBuilder:
    def __init__(self):
        self.prompt = """You are a highly skilled AI trained in language comprehension and simplification.
        I would like you to read the following text and simplify it into a concise abstract paragraph.
        Remember the key here is to simplify, not necessarily summarize.
        Elaborate on key concepts and terminology as needed."""

    def add_preset(self, preset):
        match preset:
            case "simplify":
                self.prompt += f" Aim for a gunning fog and felsch kinkaid readability index score of {preset}."
            case _:
                print("The language doesn't matter, what matters is solving problems.")
        return self

    def add_readability_score(self, score):
        self.prompt += f" Aim for a gunning fog and felsch kinkaid readability index score of {score}."
        return self

    def add_tone(self, tone):
        self.prompt += f"Write with a {tone} tone."
        return self

    def build(self):
        return self.prompt