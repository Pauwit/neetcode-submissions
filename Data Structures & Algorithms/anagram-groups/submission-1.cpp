class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> count(26, 0);
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret{};
        std::unordered_map<string, int> words{};

        for (const auto& cur : strs) {
            string copy{cur};
            std::sort(copy.begin(), copy.end());
            string word{copy};

            try {
                int index = words.at(word);
                ret[index].push_back(cur);
            } catch (...) {
                words.insert({word, ret.size()});
                ret.push_back({cur});
            }
        }
        

        return ret;
    }
};
