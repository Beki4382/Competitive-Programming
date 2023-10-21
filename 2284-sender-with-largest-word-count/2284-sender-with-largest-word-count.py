class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_word_count = {}
        
        for message, sender in zip(messages, senders):
            message_word_count = message.count(" ") + 1
            sender_word_count[sender] = sender_word_count.get(sender, 0) + message_word_count
            
        top_sender = ""
        max_word_count = 0
        
        for sender, word_count in sender_word_count.items():
            if word_count > max_word_count or (word_count == max_word_count and sender > top_sender):
                top_sender = sender
                max_word_count = word_count
                
        return top_sender

        