# Network Documentation Report

## Full Device List

| Device | Device Type | Location | Status |
|--------|-------------|----------|--------|
{% for device in devices %}
| {{ device.name }} | {{ device.device_type }} | {{ device.location }} | {{ device.status }} |
{% endfor %}

## Filtered Device List

| Device | Device Type | Location | Status |
|--------|-------------|----------|--------|
{% for device in filtered_devices %}
| {{ device.name }} | {{ device.device_type }} | {{ device.location }} | {{ device.status }} |
{% endfor %}

## Filtered Interface List

| Device | Interface | VLAN |
|--------|-----------|------|
{% for interface in filtered_interfaces %}
{% for vlan in interface.tagged_vlans %}
| {{ interface.device.name }} | {{ interface.name }} | {{ vlan.name }} |
{% endfor %}
{% endfor %}

## Management Interface Configuration

{% for device in devices %}
### {{ device.name }}

```python
[edit interfaces fxp0]
unit 0 {
    family inet {
        address {{ device.primary_ip4 }} {
            master-only;
        }
    }
}
```
{% endfor %}