"""Config flow to configure TpeWater Fee component."""
from collections import OrderedDict
from typing import Optional
import voluptuous as vol

from homeassistant.config_entries import (
    CONN_CLASS_LOCAL_PUSH,
    ConfigFlow,
    OptionsFlow,
    ConfigEntry
    )
from homeassistant.const import CONF_NAME
from homeassistant.core import callback
from homeassistant.helpers.typing import ConfigType
from .const import (
    DOMAIN,
    DEFAULT_NAME,
    CONF_WATERID,
    CONF_COOKIE,
    CONF_VIEWSTATE,
    CONF_EVENTVALIDATION
)

class LineBotFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a TpeWater Fee config flow."""

    VERSION = 1
    CONNECTION_CLASS = CONN_CLASS_LOCAL_PUSH

    def __init__(self):
        """Initialize flow."""
        self._water_id: Optional[str] = None
        self._cookie: Optional[str] = None
        self._viewstate: Optional[str] = None
        self._eventvalidation: Optional[str] = None

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry):
        """ get option flow """
        return OptionsFlowHandler(config_entry)

    async def async_step_user(
        self,
        user_input: Optional[ConfigType] = None,
        error: Optional[str] = None
    ):  # pylint: disable=arguments-differ
        """Handle a flow initialized by the user."""
        if user_input is not None:
            self._set_user_input(user_input)
            self._name = user_input.get(CONF_WATERID)
            unique_id = self._water_id
            await self.async_set_unique_id(unique_id)
            return self._async_get_entry()

        fields = OrderedDict()
        fields[vol.Required(CONF_WATERID,
                            default=self._water_id or vol.UNDEFINED)] = str
        fields[vol.Required(CONF_COOKIE,
                            default=self._cookie or vol.UNDEFINED)] = str
        fields[vol.Required(CONF_VIEWSTATE,
                            default=self._viewstate or vol.UNDEFINED)] = str
        fields[vol.Required(CONF_EVENTVALIDATION,
                            default=self._eventvalidation or vol.UNDEFINED)] = str
        self._name = self._water_id
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(fields),
            errors={'base': error} if error else None
        )

    @property
    def _name(self):
        # pylint: disable=no-member
        # https://github.com/PyCQA/pylint/issues/3167
        return self.context.get(CONF_NAME)

    @_name.setter
    def _name(self, value):
        # pylint: disable=no-member
        # https://github.com/PyCQA/pylint/issues/3167
        self.context[CONF_NAME] = value
        self.context["title_placeholders"] = {"name": self._name}

    def _set_user_input(self, user_input):
        if user_input is None:
            return
        self._water_id = user_input.get(CONF_WATERID, "")
        self._cookie = user_input.get(CONF_COOKIE, "")
        self._viewstate = user_input.get(CONF_VIEWSTATE, "")
        self._eventvalidation = user_input.get(CONF_EVENTVALIDATION, "")

    @callback
    def _async_get_entry(self):
        return self.async_create_entry(
            title=self._name,
            data={
                CONF_WATERID: self._water_id,
                CONF_COOKIE: self._cookie,
                CONF_VIEWSTATE: self._viewstate,
                CONF_EVENTVALIDATION: self._eventvalidation,
            },
        )


class OptionsFlowHandler(OptionsFlow):
    # pylint: disable=too-few-public-methods
    """Handle options flow changes."""
    _water_id = None
    _cookie = None
    _viewstate = None
    _eventvalidation = None

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage options."""
        if user_input is not None:
            self._eventvalidation = user_input.get(CONF_EVENTVALIDATION)
            self._water_id = user_input.get(CONF_WATERID)
            self._cookie = user_input.get(CONF_COOKIE)
            self._viewstate = user_input.get(CONF_VIEWSTATE)
            return self.async_create_entry(
                title='',
                data={
                    CONF_WATERID: self._water_id,
                    CONF_COOKIE: self._cookie,
                    CONF_VIEWSTATE: self._viewstate,
                    CONF_EVENTVALIDATION: self._eventvalidation,
                },
            )
        self._water_id = self.config_entry.options.get(CONF_WATERID, '')
        self._cookie = self.config_entry.options.get(CONF_COOKIE, '')
        self._viewstate = self.config_entry.options.get(CONF_VIEWSTATE, '')
        self._eventvalidation = self.config_entry.options.get(CONF_EVENTVALIDATION, '')

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_WATERID, default=self._water_id): str,
                    vol.Required(CONF_COOKIE, default=self._cookie): str,
                    vol.Required(CONF_VIEWSTATE, default=self._viewstate): str,
                    vol.Required(CONF_EVENTVALIDATION, default=self._eventvalidation): str,
                }
            ),
        )
