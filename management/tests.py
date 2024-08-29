from django.test import TestCase


def restorer(inputted, scanned, current_quantity):
    original_quantity = current_quantity

    if inputted < scanned:
        difference = scanned - inputted
        current_quantity += difference

        new_scanned = inputted
        return f'new scanned: {new_scanned}, old scanned: {scanned}, current quantity {current_quantity}, ' \
               f'original quantity {original_quantity}'
    elif scanned < inputted:
        difference = inputted - scanned
        current_quantity -= difference
        new_scanned = inputted
        return f'new scanned:{new_scanned}, old scanned: {scanned}, current quantity {current_quantity}, ' \
               f'original quantity {original_quantity}'


print(restorer(2, 4, 14))

from pos import settings
import pprint
pprint.pprint(settings.LOGGING)

# Is it also possible, my friend for certain messages or actions not to be logged in the terminal or if they ever do when they reach a certain amount they get deleted? Most of my logged messages comes from this notification function, my friend.
#
# ```
#     <script>
#
#         document.addEventListener('DOMContentLoaded', function() {
#             const notificationToggle = document.querySelector('#notification-toggle');
#             const notificationList = document.querySelector('.notification-list');
#
#             notificationToggle.addEventListener('click', () =>{
#                 notificationList.classList.toggle('notification-list-show');
#                 console.log('works');
#
#                 fetch('/seen-notifications/')
#                     .then(response => response.json())
#                     .then(data => {
#                         console.log('Notifications marked as seen:', data);
#                         // You can perform additional actions based on the response if needed
#                     })
#                     .catch(error => console.error('Error marking notifications as seen:', error));
#                     });
#         });
#
#         $(document).on('click', '.notification-delete', function() {
#             // Get notification details from the data attributes
#             var title = $(this).data('title');
#             var id = $(this).data('id');
#             var deleteUrl = '/delete-notification/' + title + '/' + id + '/';
#
#             // Make an AJAX request to remove the notification
#             $.ajax({
#                 url: deleteUrl,
#                 type: 'POST',
#                 data: {title: title, id: id, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
#                 dataType: 'json',
#                 success: function(response) {
#                     console.log(response.message);
#                     // Remove the notification from the UI if removal is successful
#                     $(this).closest('.notification').remove();
#                 },
#                 error: function(error) {
#                     console.error('Failed to remove notification', error);
#                 }
#             });
#         });
#
#         setInterval(function() {
#             $.ajax({
#                 url: '{% url "expired-products-json" %}',
#                 type: 'GET',
#                 dataType: 'json',
#                 success: function(response) {
#                     var expiredProducts = response.expired_products;
#                     var expiringProducts = response.expiring_products;
#                     var notifications = response.notification;
#                     $('.notification-counter-div').empty();
#
#                     $('#notification-list').empty();
#
#                     if (notifications.length === 0) {
#                         var emptyNotifier =
#                         `
#                             <div class="notification-empty-notifier">
#                                 No Notification
#                             </div>
#                         `;
#                         $('#notification-list').html(emptyNotifier);
#                     } else {
#                         for (var i = 0; i < notifications.length; i++) {
#                             var notification = notifications[i];
#                             var notificationCounter =
#                             `
#                                 <div class="notification-counter">
#                                     ${notification.unseen}
#                                 </div>
#                             `;
#                             var notificationHtml =
#                             `
#                                 <div class="notification">
#                                     <div class="notification-title">
#                                         ${notification.title}
#                                     </div>
#                                     <div class="notification-date-time">
#                                         ${notification.time}
#                                     </div>
#                                     <div class="notification-message">
#                                         ${notification.message}
#                                     </div>
#                                     <div class="notification-delete-div">
#                                         <a class="notification-delete" data-title="${notification.title}" data-id="${notification.id}">
#                                             Remove Notification
#                                         </a>
#                                     </div>
#                                 </div>
#                             `;
#                             if (notification.unseen !== null) {
#                                 $('.notification-counter-div').append(notificationCounter)
#                             } else {
#                                 $('.notification-counter-div').empty();
#                             };
#                             $('#notification-list').append(notificationHtml);
#                         }
#                     }
#                 }
#             });
#         }, 1000);
#     </script>
# ```
# Is it possible not to log any messages from this function, except for the error of course.