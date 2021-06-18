import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**coloredballs):
    self.BallsInTheHat=dict(coloredballs)
    self.__createcontents()
  def __createcontents(self):
    # in my opinion should be private...
    self.contents=[]
    for k in self.BallsInTheHat.keys():
      self.contents=self.contents+[k]*self.BallsInTheHat[k]
    if len(self.contents)==0:
      raise ValueError("No balls in the Hat!")
  def draw(self,balls):
    if balls>len(self.contents):
      balls=len(self.contents) # we cannot extract more balls than we have!
    extracted=random.sample(self.contents,balls)
    for extraction in extracted:
      self.contents.remove(extraction)
    return extracted
  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  good_experiment_counter=0
  for experiment in range(num_experiments):
    current_hat=copy.deepcopy(hat)
    result=current_hat.draw(num_balls_drawn)
    # we summarize the experiment in terms of a dictionary
    result_summary=dict()
    for color in result:
      result_summary[color]=result.count(color)
    # and now compare dictionaries
    good_experiment=True
    for color in expected_balls.keys():
      color_check=False
      # an experiment is positive if it contains at least as mamy
      # balls as expected of any color
      if color in result_summary.keys():
        if result_summary[color]>=expected_balls[color]:
          color_check=True
      good_experiment=good_experiment and color_check
    # if the experiment is still good after all color checks we can
    # increment the counter and return frequency based probability
    if good_experiment:
      good_experiment_counter+=1
  return good_experiment_counter/num_experiments
