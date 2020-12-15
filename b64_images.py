b64_img = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxEAAAsRAX9kX5EAAAKASURBVDhPhZTLb4xhFMZ/rapq45KGSBGJRSXWIrFgoaQLJBbd2Ikdf4CNhQ2i2NgRiQWxUITGNS61cG8piWtsUFJFQoVqjRr1O998085MpzzJ037v7TnnvOd5h0Lch2UPoOMu1KdTE+Im1Lr3vGea06kElel/bsPSCrjkZ1MVXOn4h6ib6mrgnJ9rPXPmDqzKraSCW6FmMpzwc2aM3bRk+gSiITYLzrqnKZ2q9ezxA+nZRHCfgkeh9Rf8jHGgnGgZMX7D8EnYsyWnVTEp/sgZXR58C9nlsNiSYz4W5k6B1RvglKycXSI2rN5eSz4M9xy+lwPJQRGi1a8UegODK6CxVLQWWkyhSKzVprTDLYfPZK/M5AXNnB8y89osy4nKhfEdCLHdip2FGw5tNC/lNzmSFxyRXiEDsqxoHiVi3hQv5Ff5R47ZRsRERIloXY/kJ/gSC4Xod89D0ILjxQJF0UWS6Ro37Iddc2BRbnoMdTB1Hcwzk0MG/eDUqFggmlGEi6k1ShqQzXpQM2u5HIzcbTnNOrqoisKSE5+FNUq7uROubYPLmjTuOYGZlDX/aIblTJs24IINeOxwZKUe3QHrzbQ6t2N8pskdnvalNNi5MmLRTX8Hkib02PmhiXzaAm3HdEhS8iao0uZhzAQl1uiUNhZ7QOd1jbwd2gvL1w29m9NqI0pFxnto09iNsGA+NMQLKPGZbkne+TifdsOTjXDQevtiPW+buJP6q5ak7XtUKuezceZ3b98RX4oO8NXyTg7mBePpRQaZj7lIT2UYvMi0olB0yFL7nQix5/KzzI52WYTHdAI2ke8yDhWZtgBx93qcaTICxAsbvdNCRIDCIP9DyX74Czey8LJe6Ov6AAAAAElFTkSuQmCC'
b64_pin = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAACxMAAAsTAQCanBgAAALVSURBVDhPrZTPTxNREMdnF2h3+wOB0BJFTYxEJZgeiOGHxIMJJBw8mHjSg4l6MFEOHAxRryoejBcOEk4e1YNHE/kHJEFIgFhDIZFgbQgFSne3u9vd7nvPecujoFRqop9ksjPT2W/nvXlvJRDQoaF6aWPjPqyuXmO6fobZtkss69O6aT45USh8FmVV8QXZyEg3LC29h1SqFUwTE8z/kT8Lpul8MYzLvZ43tZM8HJk9f34alpcnYX6+FQqFPTGOJEFYVYMRWX4oMlWRYW3tKSSTR8DzROpXJBRlktQqwqrIkMkMQLEowoOU8I80QmZFWBUZdN0V/gEYpfDdMLwNQl6KVFUk2tPzTMpmH0OpJFI7EOwsrWlQtG0IMfZO6eh4EIvHu0DTzjPTVD3LSm/Z9sdjm5vfxCs+UqG9vTZgGKPgukMYqyVCQHddmrNtOYiiKiZltJpQCKLxOCi4p4Cd8+G5WJcxzfGvrjt8xXH8IZTP4XQoFFIIOWdRyrYJWWmn9E0AYJAXcEFu3A9EoxBtaEBvB8t1IZnPv+hynBEelwV/Z72//yTMzKxI+by8K8qf3NRYDIKKgh5vlEFqe9uesu3m25RavK4i8c7Oew2xmMyPzX4x3+fLFnAvWFOjBhk7zuOKgmR0FCCdvhnA5Sj19WUh38JhCASDvKyMSQjBK7HO/YqCTNPCkMsd5RsfQUGlqQlqIxEINDdDBP39ODi4rOtO3mVM43FFwZKuWzjCnAhBxa7CjY2gqHzme1Cc9rKu21nP8wfCqSiojo8zVixOQF2dyByE36BFvGGZvr5H1xlLirS/PRWxE4lArWG8ll33xu4Q+ET5Od1CodVIJMXGxs7WtbVxsQtdiYR/f/8oyHnb0gK9jnMR13a1ROmpIqUlw/MWtwj5kGJs9tLc3C0se4U2gYLD/kv/yvTCQjfaD7RBHh/a4d+CYvzzxju9818EOSiKVwcGfgIZz0q94tsQ2gAAAABJRU5ErkJggg=='
continue_b64 = b'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'