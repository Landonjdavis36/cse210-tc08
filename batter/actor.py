from game import constants
from game.point import Point

class Actor:artifact"""A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position artifactand velocity in 2d space.
artifactStereotype:artifact    Information Holder
artifactAttributes:artifact    _tag (string): The actor's tag.artifact    _text (string): The textual representation of the actor.artifact    _position (Point): The actor's position in 2d space.artifact    _velocity (Point): The actor's speed and direction.artifact"""
artifactdef __init__(self):artifact    """The class constructor."""artifact    self._description = ""artifact    self._text = ""artifact    self._position = Point(0, 0)artifact    self._velocity = Point(0, 0)
artifactdef get_description(self):artifact    """Gets the artifact's description.artifact    artifact    Returns:artifact        string: The artifact's description.artifact    """artifact    return self._description 
artifactdef get_position(self):artifact    """Gets the actor's position in 2d space.artifact    artifact    Returns:artifact        Point: The actor's position in 2d space.artifact    """artifact    return self._positionartifactartifactdef get_text(self):artifact    """Gets the actor's textual representation.artifact    artifact    Returns:artifact        string: The actor's textual representation.artifact    """artifact    return self._text
artifactdef get_velocity(self):artifact    """Gets the actor's speed and direction.artifact    artifact    Returns:artifact        Point: The actor's speed and direction.artifact    """artifact    return self._velocityartifactartifactdef set_description(self, description):artifact    """Updates the actor's description to the given one.artifact    artifact    Args:artifact        description (string): The given description.artifact    """artifact    self._description = description
artifactdef set_position(self, position):artifact    """Updates the actor's position to the given one.artifact    artifact    Args:artifact        position (Point): The given position.artifact    """artifact    self._position = positionartifactartifactdef set_text(self, text):artifact    """Updates the actor's text to the given value.artifact    artifact    Args:artifact        text (string): The given value.artifact    """artifact    self._text = text
artifactdef set_velocity(self, velocity):artifact    """Updates the actor's velocity to the given one.artifact    artifact    Args:artifact        position (Point): The given velocity.artifact    """artifact    self._velocity = velocity