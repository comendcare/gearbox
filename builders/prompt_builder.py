class PromptBuilder:
    def __init__(self):
        self.prompt = """You are a highly skilled AI trained in language comprehension and simplification. 
        I would like you to read the following text and simplify it.
        Remember the key here is to simplify, not necessarily summarize.
        Follow the same structure and logic as the input and elaborate on key concepts and terminology as needed."""

    def add_preset(self, preset):
        match preset:
            case "simplify":
                self.prompt += """ Respectfully and with dignity, explain the content as if you were speaking to a 
                                    newcomer to the topic."""
            case "terminology":
                self.prompt += """ Identify the key terminology and concepts in point form and explain each using 
                                    analogies and comparisons. Break down the acronyms and medical jargon, taking extra 
                                    care to be as accurate and correct as possible."""
            case "applications":
                self.prompt += """ Describe the applications of the content, and the implications that this research 
                                    has on the field. Answer with why this research is important and necessary."""
            case "optimistic":
                self.prompt += """ Optimistically identify the directions that this research can go, and the potential 
                                    benefits for the user."""
            case "analyzed":
                self.prompt += """ Objectively and realistically analyze the key results and outcomes of the content. 
                                    list the most promising and clear statistics if provided in the content."""
            case "takeaways":
                self.prompt += """ List the key takeaways from the content. They should be comprehensive and make no 
                                    inferences beyond that the information provided in the content."""
            case "takeaways":
                self.prompt += """ Answer the 6 questions in a list: 
                                     (1) What do the author(s) want to know (motivation)?
                                     (2) What did they do (approach/methods)?
                                     (3) Why was it done that way (context within the field)?
                                     (4) What do the results show (figures and data tables)?
                                     (5) How did the author(s) interpret the results (interpretation/discussion)?
                                     (6) What should be done next?
                                     (Regarding this last question, the author(s) may provide some suggestions in the 
                                     discussion, but the key is to ask yourself what you think should come next.) """
            case _:
                print("The language doesn't matter, what matters is solving problems.")
        return self

    def add_readability_score(self, score):
        min_gunning_fog = 6  # Most readable
        gunning_fog_range = 14  # 6+14 = 20 a.k.a least readable
        mapped_value = min_gunning_fog + (score * gunning_fog_range)
        gf_index_score = round(mapped_value, 2)

        min_fk_score = 100  # Most readable
        max_fk_score = 0  # Least readable
        fk_range = min_fk_score - max_fk_score
        mapped_value = min_fk_score - ((1 - score) * fk_range)
        fk_index_score = round(mapped_value, 2)

        self.prompt += f" Aim for a gunning fog readability index score of {gf_index_score}."
        self.prompt += f" Aim for a felsch kinkaid readability index score of {fk_index_score}."
        return self

    def add_tone(self, tone):
        self.prompt += f"Write with a {tone} tone."
        return self

    def build(self):
        return self.prompt