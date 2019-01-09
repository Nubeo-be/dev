/* Odoo web_ressources
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */


odoo.define('web_ressources.RessourcesView', function (require) {
    "use strict";

    var core = require('web.core');
    var view_registry = require('web.view_registry');
    var AbstractView = require('web.AbstractView');

    var _lt = core._lt;

    var RessourcesView = AbstractView.extend({
        display_name: _lt('Ressources'),
        icon: 'fa-clock-o',
    });
    view_registry.add('ressources', RessourcesView);
    return RessourcesView;
});