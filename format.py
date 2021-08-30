# formating in python 

# have two most important method 

# method 1

channel_name="catch error"
channel_type="coding"
channel_link="https://www.youtube.com/channel/UCgxaL_Yx-yqG2A7-RbY6x2w"
channel_subscribe=False

# if(channel_subscribe!=True):
#     print("please subscribe my channel my channel name is {0} and channel type is {1} and channel link is {2}".format(channel_name,channel_type,channel_link))

# else:
#     print("you already subscribe my channel name {0}".format(channel_name))

 

#  this is second way of method first


# if(channel_subscribe!=True):
#     print("please subscribe my channel my channel name is {channel_name} and channel type is {channel_type} and channel link is {channel_link}".format(channel_name=channel_name,channel_type=channel_type,channel_link=channel_link))

# else:
#     print("you already subscribe my channel name {channel_name}".format(channel_name=channel_name))

#method 2 for formating in python
# in this method we can use f keyword and we get same output which we get using first method 

# this method is very suitable and most used method for formating in python


if(channel_subscribe!=True):
    print(f"please subscribe my channel my channel name is {channel_name} and channel type is {channel_type} and channel link is {channel_link}")

else:
    print(f"you already subscribe my channel name {channel_name} ")



print(f'thanks for watching my video and please do subscribe my channel {channel_name} and like the video and share the link channel link {channel_link}')    




