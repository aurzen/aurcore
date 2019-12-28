# import asyncio
# import typing as ty
# from datetime import datetime, timedelta
#
# import discord
# import functools
# import abc
# import collections
# from aurcore.utils.discord import send_to
# from aurcore.utils.time import parse_time
# import aurcore as ac
# import aurcore.event
# import aurcore.task.context
#
#
# class Action(abc.ABC):
#     def __init__(self, func, context: ac.task.context, name=None):
#         self.func = func
#         self.context = context
#         self.name = name or self.func.__name__
#
#     def __repr__(self):
#         return f"Action {self.name} in {self.context}}"
#     pass
#
# class CommandAction(Action):
#     pass
#
# #
# class AutoAction(Action):
#     pass
#
#
# # class InstantAutoAction(AutoAction):
# #     pass
# #
# #
# # class ResumableAutoAction(AutoAction):
# #     pass
# #
# #
# # class EventedAction(Action):
# #     @abc.abstractmethod
# #     def hooks(self):
# #         pass
# #
# #
# # class ActionRunner:
# #     def __init__(self):
# #         self.autos: ty.Dict[aurcore.event.Event, ty.List[Action]] = collections.defaultdict(list)
# #
# #     def submit(self, action: Action):
# #         if isinstance(action, AutoAction):
# #             for hook in action.hooks():
# #                 self.autos[hook].append(action)
# #         else:
# #             pass
# # #
# #
# # class TimedAutoAction(AutoAction, abc.ABC):
# #
# #     def __init__(self, dt_end: datetime, action: callable,
# #                  callback: callable = lambda x: x,
# #                  action_kwargs: dict = None):
# #         self.dt_end = dt_end
# #         self.action = action
# #         self.action_kwargs = action_kwargs or {}
# #         self.asynchro = False
# #         self.callback = callback
# #
# #     def is_done(self):
# #         return datetime.utcnow() > self.dt_end
# #
# #     def tick(self):
# #         if datetime.utcnow() > self.dt_end:
# #             self.execute()
# #
# #     def execute(self):
# #         if isinstance(self.action):
# #             task = asyncio.create_task(self.action(**self.action_kwargs))
# #             task.add_done_callback(self.callback)
# #         else:
# #             return self.callback(self.action(**self.action_kwargs))
# #
# #
# # class Reminder(TimedAutoAction):
# #     def __init__(self, text, time_inp: ty.Union[datetime, timedelta, str, int],
# #                  output: ty.Union[discord.abc.Messageable, int] = None):
# #         action = functools.partial(send_to, destination=output, content=text)
# #         super().__init__(dt_end=parse_time(time_inp), action=action)
