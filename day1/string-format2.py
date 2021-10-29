l = "admin:$E*G$@R:/users/root:"

words = l.split(':')

print("User    \t:%s"%words[0])
print("Password\t:%s"%words[1])
print("Homedir \t:%s"%words[2])

