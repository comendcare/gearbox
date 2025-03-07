class TranslationPromptBuilder:
    def __init__(self):
        self.prompt = """You are a highly skilled AI trained in language comprehension and simplification. 
                        I would like you to read the following text and simplify it. Do not use first person.
                        Remember the key here is to simplify, not necessarily summarize.
                        Provide only the output don't reply as if you're talking to someone."""

    def add_audience(self, audience):
        match audience:
            case "FAMILY":
                self.prompt += """ You are talking to a family member or perhaps even a subject personally affected by
                                    the topic of the content. Explain the content as if you were speaking to a newcomer
                                    to the topic. Identify the key terminology and concepts and explain each using
                                    analogies and comparisons. Break down the acronyms and medical jargon, taking extra
                                    care to be accurate and correct."""
                # self.prompt += ""
            case "SCIENTIST":
                self.prompt += """ You are talking to a scientist, or someone who is extremely knowledgeable in the 
                                    topic of this content. Summarize the findings. If there is a method, distill it into 
                                    a step by step process. Compare the content to similar research. Be objecive and 
                                    empirical, make the potential limitations of the content clear. Use headings, bold 
                                    and italic fonts, bullet points, numbered lists, hyperlinks, quote the paper, and 
                                    use other rich text. Write your output in Markdown. Cite your sources with 
                                    hyperlinks."""
            case "INDUSTRY":
                self.prompt += """ You are an industry professional. Someone in business or product development. 
                                    Identify the potential products that could be derived and asses the feasibility of 
                                    these products. Identify existing products and more business focused insights."""
            case "DONOR":
                self.prompt += """ You are a potential investor. You are considering investing or funding a project on 
                                    the topic of this content. Have a paragraph highlighting how a potential investment 
                                    can support this research and those it affects."""
            case "WIKIPEDIA":
                self.prompt += """ You are are writing a Wikipedia article on the prompt. Structure the output 
                                    chronologically, in a way that can be easily understood by any reader. Use headings, 
                                    reference real world events outside of the provided content and relevant contextual 
                                    information. Use headings, bold and italic fonts, bullet points, numbered lists, 
                                    hyperlinks, quote the paper, and use other rich text. Write your output in Markdown. 
                                    Cite your sources with hyperlinks."""
            case "SOCIALS":
                self.prompt += """ Write a caption appropriate for use on Instagram, Facebook, Twitter, and LinkedIn. 
                                    Keep it succinct and to the point. Output must be less than 50 words. 
                                    If appropriate, provide a list of hashtags."""
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
        # min_gunning_fog = 6  # Most readable
        # gunning_fog_range = 14  # 6+14 = 20 a.k.a least readable
        # mapped_value = min_gunning_fog + (score * gunning_fog_range)
        # gf_index_score = round(mapped_value, 2)

        # Define the ranges for user score and Gunning Fog score
        user_min, user_max = 0, 10
        fog_min, fog_max = 20, 0  # Reversed scale

        # Apply the linear transformation
        gf_index_score = ((score - user_min) * (fog_max - fog_min) / (user_max - user_min)) + fog_min

        fk_index_score = score * 10

        self.prompt += f" Aim for a gunning fog readability index score of {gf_index_score}."
        self.prompt += f" Aim for a felsch kinkaid readability index score of {fk_index_score}."

        return self

    def add_tone(self, tone):
        self.prompt += f" Write with a {tone.lower()} tone."
        return self

    def build(self):
        return ' '.join(self.prompt.strip().split())

