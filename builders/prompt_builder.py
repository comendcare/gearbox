class PromptBuilder:
    def __init__(self):
        self.prompt = """You are a highly skilled AI trained in language comprehension and simplification. 
        I would like you to read the following text and simplify it.
        Remember the key here is to simplify, not necessarily summarize.
        Follow the same structure and logic as the input and elaborate on key concepts and terminology as needed."""

    def add_audience(self, audience):
        match audience:
            case "FAMILY":
                self.prompt += """ You are talking to a family member or perhaps even a subject personally affected by 
                                    the topic of the content. Respectfully and with dignity, explain the content as if 
                                    you were speaking to a newcomer to the topic. Identify the key terminology and 
                                    concepts in point form and explain each using analogies and comparisons. Break down 
                                    the acronyms and medical jargon, taking extra care to be accurate and correct. """
            case "SCIENTIST":
                self.prompt += """ You are talking to a scientist, or someone who is extremely knowledgeable in the 
                                    topic of this content. Summarize the findings. If there is a method, distill it into 
                                    a step by step process. Compare the content to similar research."""
            case "INDUSTRY":
                self.prompt += """ You are an industry professional. Someone in business or product development. 
                                    Summarize the potential products that could be derived and asses the feasibility of 
                                    these products. Identify existing products and more business focused insights."""
            case "INVESTOR":
                self.prompt += """ You are a potential investor. You are considering investing or funding a project on 
                                    the topic of this content. Have a paragraph highlighting how a potential investment 
                                    can support this research and those it affects."""
            case _:
                # If an audience isn't defined, just skip it. In this case, a preset should be provided.
                pass
        return self

    def add_preset(self, preset):
        match preset:
            case "SIMPLIFY":
                self.prompt += """ Respectfully and with dignity, explain the content as if you were speaking to a 
                                    newcomer to the topic."""
            case "TERMINOLOGY":
                self.prompt += """ Identify the key terminology and concepts in point form and explain each using 
                                    analogies and comparisons. Break down the acronyms and medical jargon, taking extra 
                                    care to be as accurate and correct as possible."""
            case "APPLICATIONS":
                self.prompt += """ Describe the applications of the content, and the implications that this research 
                                    has on the field. Answer with why this research is important and necessary."""
            case "OPTIMISTIC":
                self.prompt += """ Optimistically identify the directions that this research can go, and the potential 
                                    benefits for the user."""
            case "ANALYZED":
                self.prompt += """ Objectively and realistically analyze the key results and outcomes of the content. 
                                    list the most promising and clear statistics if provided in the content."""
            case "TAKEAWAYS":
                self.prompt += """ List the key takeaways from the content. They should be comprehensive and make no 
                                    inferences beyond that the information provided in the content."""
            case "QUESTIONS":
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
                # If a preset isn't defined or doesn't match, just skip it. In this case, an audience should be provided.
                pass
        return self

    def add_readability_score(self, score):
        min_gunning_fog = 6  # Most readable
        gunning_fog_range = 14  # 6+14 = 20 a.k.a least readable
        mapped_value = min_gunning_fog + (score * gunning_fog_range)
        gf_index_score = round(mapped_value, 2)

        min_fk_score = 100  # Most readable
        max_fk_score = 0  # Least readable
        fk_range = min_fk_score - max_fk_score
        mapped_value = min_fk_score - ((10 - score) * fk_range)
        fk_index_score = round(mapped_value, 2)

        self.prompt += f" Aim for a gunning fog readability index score of {gf_index_score}."
        self.prompt += f" Aim for a felsch kinkaid readability index score of {fk_index_score}."
        return self

    def add_tone(self, tone):
        self.prompt += f" Write with a {tone.lower()} tone."
        return self

    def build(self):
        return self.prompt