#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <new_app_name>"
  exit 1
fi

OLD="portal"
NEW="$1"

# Derive class names
# e.g. portal → Portal; then add Config or Setting
UPPER_OLD="$(echo ${OLD:0:1} | tr '[:lower:]' '[:upper:]')${OLD:1}"
UPPER_NEW="$(echo ${NEW:0:1} | tr '[:lower:]' '[:upper:]')${NEW:1}"
OLD_CFG_CLASS="${UPPER_OLD}Config"
NEW_CFG_CLASS="${UPPER_NEW}Config"
OLD_SETTING_CLASS="${UPPER_OLD}Setting"
NEW_SETTING_CLASS="${UPPER_NEW}Setting"

echo "Cloning '$OLD' → '$NEW'..."
cp -R web/$OLD web/$NEW

echo "Replacing module names and class names inside files..."
# Replace bare module references
grep -RIl "\b$OLD\b" web/$NEW | xargs sed -i "s/\b$OLD\b/$NEW/g"
# Replace config class names
grep -RIl "$OLD_CFG_CLASS" web/$NEW | xargs sed -i "s/$OLD_CFG_CLASS/$NEW_CFG_CLASS/g"
# Replace Setting class names
grep -RIl "$OLD_SETTING_CLASS" web/$NEW | xargs sed -i "s/$OLD_SETTING_CLASS/$NEW_SETTING_CLASS/g"

echo
echo "✅ App cloned to web/$NEW/"
echo
echo "Next steps:"
echo "1) Add to INSTALLED_APPS in settings.py:"
echo "     'portal.apps.PortalConfig',"
echo "     '$NEW.apps.$NEW_CFG_CLASS',"
echo "2) Include its URLs in urls.py:"
echo "     path('$NEW/', include('$NEW.urls', namespace='$NEW'))"
echo "3) Run migrations:"
echo "     docker-compose exec web python manage.py makemigrations $NEW"
echo "     docker-compose exec web python manage.py migrate"
echo "4) Restart your services."
