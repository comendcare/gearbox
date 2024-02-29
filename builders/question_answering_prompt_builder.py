class QuestionAnsweringPromptBuilder:
    def __init__(self):
        self.prompt = """
        You are a highly skilled AI capable of having nuanced discussions with rare disease families on finding rare disease resources.
        You are effectively a concierge for https://www.librarey.com/
        Keep responses concise and don't make risky recommendations.
        """

    def add_preset(self, preset):
        match preset:
            case "RECOMMEND":
                self.prompt += """ Recommend the top 1-5 resources that might be helpful to the user."""
            case "NAVIGATE":
                self.prompt += """ Refer the user to the correct FAQ guide or tell them how they can achieve their goal.
                """
        return self

    def build(self):
        return ' '.join(self.prompt.strip().split())
