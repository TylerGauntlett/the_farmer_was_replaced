import world_handler
import unlock_handler

while True:
	unlock_handler.auto_unlock()
	world_handler.setup()
	world_handler.handle()